# ZDI-11-330: InduSoft WebStudio Unauthenticated Remote Operations Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-330
- **ZDI-CAN:** ZDI-CAN-1181
- **Date:** 2011-11-16
- **CVE:** CVE-2011-4051
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Indusoft
- **Affected Products:** WebStudio
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-330/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Indusoft Web Studio. Authentication is not required to exploit this vulnerability. The flaw exists within the Remote Agent component (CEServer.exe) which listens by default on TCP port 4322. When handling incoming requests the process fails to perform any type of authentication. Many available operations allow direct manipulation and creation of files on disk, loading of arbitrary DLLs and process control. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the User.

## Additional Details

Indusoft has issued an update to correct this vulnerability. More details can be found at: http://www.indusoft.com/hotfixes/hotfixes.php

## Disclosure Timeline

- 2011-04-27 - Vulnerability reported to vendor
- 2011-11-16 - Coordinated public release of advisory
