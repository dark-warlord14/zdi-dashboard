# ZDI-25-267: GStreamer H265 Codec Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-267
- **ZDI-CAN:** ZDI-CAN-26596
- **Date:** 2025-04-30
- **CVE:** CVE-2025-3887
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GStreamer
- **Affected Products:** GStreamer
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-267/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GStreamer. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of H265 slice headers. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GStreamer has issued an update to correct this vulnerability. More details can be found at: https://gitlab.freedesktop.org/tpm/gstreamer/-/commit/d0e18d6353e4e448ccf3b06a967b394e664dd0b5

## Disclosure Timeline

- 2025-03-07 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-07-03 - Advisory Updated
