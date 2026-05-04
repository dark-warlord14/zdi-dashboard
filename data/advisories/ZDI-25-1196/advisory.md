# ZDI-25-1196: GIMP PSP File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1196
- **ZDI-CAN:** ZDI-CAN-28232
- **Date:** 2025-12-29
- **CVE:** CVE-2025-15059
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1196/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PSP files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GIMP has issued an update to correct this vulnerability. More details can be found at: https://gitlab.gnome.org/GNOME/gimp/-/commit/03575ac8cbb0ef3103b0a15d6598475088dcc15e

## Disclosure Timeline

- 2025-11-11 - Vulnerability reported to vendor
- 2025-12-29 - Coordinated public release of advisory
- 2025-12-29 - Advisory Updated
