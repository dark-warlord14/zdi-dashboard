# ZDI-26-283: GStreamer qtdemux Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-283
- **ZDI-CAN:** ZDI-CAN-29392
- **Date:** 2026-04-15
- **CVE:** CVE-2026-5056
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GStreamer
- **Affected Products:** GStreamer
- **Credit:** DongHyeon Hwang (kind_killerwhale)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-283/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GStreamer. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of UncompressedFrameConfigBox structures. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GStreamer has issued an update to correct this vulnerability. More details can be found at: https://gitlab.freedesktop.org/api/v4/projects/gstreamer%2Fgstreamer/repository/files/security-advisories%2Fsa-2026-0016.md/raw?ref=main

## Disclosure Timeline

- 2026-03-12 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
