# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/asiakirjasuodatin/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([6dd09939 ...](https://git.sr.ht/~sthagen/asiakirjasuodatin/blob/default/etc/sbom/cdx.json.sha256 "sha256:6dd09939f2c1603ea4e86078d8e24b8c81db58fae5bf5fae1ab1ebf3b1b7c482")).
<!--[[[end]]] (checksum: 03fd1843fef27f3adb93e0a21718c5d6)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                 | Version                                                | License     | Author          | Description (from packaging data)                                                                        |
|:-----------------------------------------------------|:-------------------------------------------------------|:------------|:----------------|:---------------------------------------------------------------------------------------------------------|
| [msgspec](https://jcristharif.com/msgspec/)          | [0.17.0](https://pypi.org/project/msgspec/0.17.0/)     | BSD License | Jim Crist-Harif | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
| [pandocfilters](http://github.com/jgm/pandocfilters) | [1.5.0](https://pypi.org/project/pandocfilters/1.5.0/) | BSD License | John MacFarlane | Utilities for writing pandoc filters in python                                                           |
<!--[[[end]]] (checksum: f5d32acf2fc4a273c8f1a4de420a00d5)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name | Version | License | Author | Description (from packaging data) |
|:-----|:--------|:--------|:-------|:----------------------------------|
<!--[[[end]]] (checksum: 8a87b89207db0be2864af66f9266660c)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
msgspec==0.17.0
pandocfilters==1.5.0
````
<!--[[[end]]] (checksum: dc25039813eb50ca86eb08ae4a071c34)-->
