# ZDI-23-1007: GStreamer RealMedia File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1007
- **ZDI-CAN:** ZDI-CAN-21443
- **Date:** 2023-07-27
- **CVE:** CVE-2023-38103
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GStreamer
- **Affected Products:** GStreamer
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1007/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GStreamer. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of MDPR chunks. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GStreamer has issued an update to correct this vulnerability. More details can be found at: https://gitlab.freedesktop.org/gstreamer/gstreamer/uploads/d4a0aa4ec2165f6c418703b9e1459d8b/0002-rmdemux-Check-for-integer-overflow-when-calculation-.patch

## Disclosure Timeline

- 2023-07-06 - Vulnerability reported to vendor
- 2023-07-27 - Coordinated public release of advisory
