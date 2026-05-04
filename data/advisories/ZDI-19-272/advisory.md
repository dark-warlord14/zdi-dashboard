# ZDI-19-272: Microsoft Windows DHCP Client Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-272
- **ZDI-CAN:** ZDI-CAN-7822
- **Date:** 2019-03-12
- **CVE:** CVE-2019-0726
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Saran Neti of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-272/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DHCP Client service. A crafted DHCP packet can trigger an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the Local Service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0726

## Disclosure Timeline

- 2019-01-11 - Vulnerability reported to vendor
- 2019-03-12 - Coordinated public release of advisory
- 2019-04-01 - Advisory Updated
