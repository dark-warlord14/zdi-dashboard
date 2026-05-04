# ZDI-23-842: VMware Aria Operations for Networks exportPDF Code Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-842
- **ZDI-CAN:** ZDI-CAN-20778
- **Date:** 2023-06-08
- **CVE:** CVE-2023-20889
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Aria Operations for Networks
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-842/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of VMware Aria Operations for Networks. Authentication is required to exploit this vulnerability. The specific flaw exists within the exportPDF method. The issue results from the lack of proper validation of a user-supplied string before using it to execute JavaScript code. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0012.html

## Disclosure Timeline

- 2023-04-13 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
