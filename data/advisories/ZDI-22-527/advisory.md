# ZDI-22-527: (Pwn2Own) Netatalk parse_entries Improper Handling of Exceptional Conditions Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-527
- **ZDI-CAN:** ZDI-CAN-15819
- **Date:** 2022-03-23
- **CVE:** CVE-2022-23121
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Netatalk
- **Affected Products:** Netatalk
- **Credit:** NCC Group EDG (Alex Plaskett, Cedric Halbronn, Aaron Adams)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-527/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Netatalk. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parse_entries function. The issue results from the lack of proper error handling when parsing AppleDouble entries. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Netatalk has issued an update to correct this vulnerability. More details can be found at: https://netatalk.sourceforge.io/3.1/ReleaseNotes3.1.13.html

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
