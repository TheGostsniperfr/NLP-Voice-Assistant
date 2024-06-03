{
  description = "Simple flake to dev on our Python NLP project";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs, ...}:
  let system = "x86_64-linux";
  pkgs = nixpkgs.legacyPackages.${system};
  in
  {
    devShells.${system}.default = pkgs.mkShell {
      buildInputs = with pkgs; [
        git
        python311
        #python311Packages.numpy
        #python311Packages.nltk
        python311Packages.flet
];

    shellHook = ''
      clear
      echo "Welcome to the flake :)"
    '';

  };
  };
}
