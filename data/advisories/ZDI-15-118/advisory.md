# ZDI-15-118: IBM Tivoli Storage Manager FastBack Mount CMountDismount::GetVaultDump Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-118
- **ZDI-CAN:** ZDI-CAN-2667
- **Date:** 2015-04-08
- **CVE:** CVE-2015-0119
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** Brian Gorenc - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-118/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Storage Manager FastBack. Authentication is not required to exploit this vulnerability. The specific flaw exists within FastBackServer.exe which listens by default on TCP port 30051. When handling opcode 0x09 packets, the process blindly copies user supplied data into a stack-based buffer within CMountDismount::GetVaultDump. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21699645

## Disclosure Timeline

- 2015-01-08 - Vulnerability reported to vendor
- 2015-04-08 - Coordinated public release of advisory
