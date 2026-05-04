# ZDI-23-1797: Schneider Electric C-Bus Toolkit TransferCommand Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1797
- **ZDI-CAN:** ZDI-CAN-21115
- **Date:** 2023-12-15
- **CVE:** CVE-2023-5402
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** C-Bus Toolkit
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1797/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric C-Bus Toolkit. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TransferCommand command. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-306-06

## Disclosure Timeline

- 2023-07-13 - Vulnerability reported to vendor
- 2023-12-15 - Coordinated public release of advisory
