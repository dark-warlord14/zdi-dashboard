# ZDI-25-912: GIMP WBMP File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-912
- **ZDI-CAN:** ZDI-CAN-27878
- **Date:** 2025-09-24
- **CVE:** CVE-2025-10923
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-912/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WBMP files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GIMP has issued an update to correct this vulnerability. More details can be found at: https://gitlab.gnome.org/GNOME/gimp/-/commit/2d2d39f3da1d0b01ca7d71ad2b7a8725ee92ed96

## Disclosure Timeline

- 2025-09-02 - Vulnerability reported to vendor
- 2025-09-24 - Coordinated public release of advisory
- 2025-09-24 - Advisory Updated
