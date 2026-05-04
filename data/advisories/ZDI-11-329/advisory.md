# ZDI-11-329: InduSoft WebStudio CEServer Operation 0x15 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-329
- **ZDI-CAN:** ZDI-CAN-1183
- **Date:** 2011-11-16
- **CVE:** CVE-2011-4052
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Indusoft
- **Affected Products:** WebStudio
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-329/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Indusoft WebStudio. Authentication is not required to exploit this vulnerability. The flaw exists within the CEServer component which is used as a runtime dependency for applications deployed using Indusoft WebStudio. When handling the Remove File operation (0x15) the process blindly copies user supplied data to a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

Indusoft has issued an update to correct this vulnerability. More details can be found at: http://www.indusoft.com/hotfixes/hotfixes.php

## Disclosure Timeline

- 2011-04-27 - Vulnerability reported to vendor
- 2011-11-16 - Coordinated public release of advisory
