# ZDI-22-529: (Pwn2Own) Netatalk setfilparams Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-529
- **ZDI-CAN:** ZDI-CAN-15837
- **Date:** 2022-03-23
- **CVE:** CVE-2022-23122
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Netatalk
- **Affected Products:** Netatalk
- **Credit:** Orange Tsai (@orange_8361) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-529/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Netatalk. Authentication is not required to exploit this vulnerability. The specific flaw exists within the setfilparams function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Netatalk has issued an update to correct this vulnerability. More details can be found at: https://netatalk.sourceforge.io/3.1/ReleaseNotes3.1.13.html

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
