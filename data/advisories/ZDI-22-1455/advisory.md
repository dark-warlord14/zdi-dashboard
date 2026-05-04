# ZDI-22-1455: (Pwn2Own) Kepware KEPServerEX Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1455
- **ZDI-CAN:** ZDI-CAN-18411
- **Date:** 2022-10-21
- **CVE:** CVE-2022-2825
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Kepware
- **Affected Products:** KEPServerEX
- **Credit:** Vera Mens, Uri Katz, Sharon Brizinov of Claroty Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1455/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Kepware KEPServerEX. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of text encoding conversions. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Kepware has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-242-10

## Disclosure Timeline

- 2022-08-18 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
