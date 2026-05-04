# ZDI-23-1647: GStreamer MXF File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1647
- **ZDI-CAN:** ZDI-CAN-22299
- **Date:** 2023-11-15
- **CVE:** CVE-2023-44446
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GStreamer
- **Affected Products:** GStreamer
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1647/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GStreamer. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of MXF video files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GStreamer has issued an update to correct this vulnerability. More details can be found at: https://gstreamer.freedesktop.org/security/sa-2023-0010.html

## Disclosure Timeline

- 2023-10-19 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
