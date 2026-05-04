# ZDI-26-166: GStreamer rtpqdm2depay Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-166
- **ZDI-CAN:** ZDI-CAN-28850
- **Date:** 2026-03-06
- **CVE:** CVE-2026-3083
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GStreamer
- **Affected Products:** GStreamer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-166/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GStreamer. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the processing of X-QDM RTP payload elements. When parsing the packetid element, the process does not properly validate user-supplied data, which can result in a write past the end of an allocated array. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GStreamer has issued an update to correct this vulnerability. More details can be found at: https://gitlab.freedesktop.org/gstreamer/gstreamer/-/commit/d60a94dee3c0a0942c9981491bf83e0de1900fbf

## Disclosure Timeline

- 2026-02-06 - Vulnerability reported to vendor
- 2026-03-06 - Coordinated public release of advisory
- 2026-03-06 - Advisory Updated
