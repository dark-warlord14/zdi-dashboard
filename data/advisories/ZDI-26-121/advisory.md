# ZDI-26-121: GIMP XWD File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-121
- **ZDI-CAN:** ZDI-CAN-28591
- **Date:** 2026-02-19
- **CVE:** CVE-2026-2048
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-121/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XWD files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GIMP has issued an update to correct this vulnerability. More details can be found at: https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2586/diffs?commit_id=57712677007793118388c5be6fb8231f22a2b341

## Disclosure Timeline

- 2025-12-24 - Vulnerability reported to vendor
- 2026-02-19 - Coordinated public release of advisory
- 2026-02-19 - Advisory Updated
