# ZDI-22-1464: GnuPG libksba CMS File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1464
- **ZDI-CAN:** ZDI-CAN-18929
- **Date:** 2022-10-25
- **CVE:** CVE-2022-3515
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** GnuPG
- **Affected Products:** libksba
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1464/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GnuPG libksba. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of CMS files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GnuPG has issued an update to correct this vulnerability. More details can be found at: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1021928

## Disclosure Timeline

- 2022-10-04 - Vulnerability reported to vendor
- 2022-10-25 - Coordinated public release of advisory
