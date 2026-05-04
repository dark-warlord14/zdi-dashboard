# ZDI-15-549: AlienVault Unified Security Management av-forward Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-549
- **ZDI-CAN:** ZDI-CAN-2992
- **Date:** 2015-11-10
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** AlienVault
- **Affected Products:** Unified Security Management
- **Credit:** agix
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-549/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault Unified Security Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within the av-forward Python daemon. A remote attacker can cause the daemon to deserialize arbitrary cPickle objects. This vulnerability can be leveraged to gain remote code execution under the context of the avforw account.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: https://www.alienvault.com/forums/discussion/5830/

## Disclosure Timeline

- 2015-06-25 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
