# ZDI-24-783: PaperCut MF pc-upconnector-service Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-783
- **ZDI-CAN:** ZDI-CAN-23116
- **Date:** 2024-06-18
- **CVE:** CVE-2024-1884
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** PaperCut
- **Affected Products:** MF
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-783/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PaperCut MF. Authentication is not required to exploit this vulnerability. The specific flaw exists within the pc-upconnector-service service, which listens on TCP port 9151 by default. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/Security-Bulletin-March-2024

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
