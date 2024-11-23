{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { nixpkgs, ... }:
    let

      pkgsForSystem = system:
        import nixpkgs {
          inherit system;
        };
      pkgs = pkgsForSystem "x86_64-linux";
      py = pkgs.python3.withPackages (python-pkgs: [
        python-pkgs.flask
      ]);
    in
    {
      packages."x86_64-linux".default = pkgs.writeShellScriptBin "totpal" ''
        ${py}/bin/python3 ${./server.py} ${./index.html}
      '';
    };

}
