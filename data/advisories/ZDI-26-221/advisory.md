# ZDI-26-221: GIMP XPM File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-221
- **ZDI-CAN:** ZDI-CAN-28901
- **Date:** 2026-03-19
- **CVE:** CVE-2026-4154
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-221/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XPM files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GIMP has issued an update to correct this vulnerability. More details can be found at: https://gitlab.gnome.org/GNOME/gimp/-/commit/2e7ed91793792d9e980b2df4c829e9aa60459253

## Disclosure Timeline

- 2026-03-05 - Vulnerability reported to vendor
- 2026-03-19 - Coordinated public release of advisory
- 2026-03-19 - Advisory Updated
