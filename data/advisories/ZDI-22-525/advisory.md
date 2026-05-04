# ZDI-22-525: (Pwn2Own) Netatalk get_finderinfo Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-525
- **ZDI-CAN:** ZDI-CAN-15870
- **Date:** 2022-03-23
- **CVE:** CVE-2022-23124
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Netatalk
- **Affected Products:** Netatalk
- **Credit:** Theori (@theori_io)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-525/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Netatalk. Authentication is not required to exploit this vulnerability. The specific flaw exists within the get_finderinfo method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Netatalk has issued an update to correct this vulnerability. More details can be found at: https://netatalk.sourceforge.io/3.1/ReleaseNotes3.1.13.html

## Disclosure Timeline

- 2021-12-08 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
