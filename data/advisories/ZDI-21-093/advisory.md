# ZDI-21-093: Schneider Electric IGSS CGF File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-093
- **ZDI-CAN:** ZDI-CAN-11271
- **Date:** 2021-01-29
- **CVE:** CVE-2020-7554
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-093/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric IGSS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CGF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.se.com/ww/en/download/document/SEVD-2020-315-03/

## Disclosure Timeline

- 2020-08-07 - Vulnerability reported to vendor
- 2021-01-29 - Coordinated public release of advisory
- 2021-01-29 - Advisory Updated
