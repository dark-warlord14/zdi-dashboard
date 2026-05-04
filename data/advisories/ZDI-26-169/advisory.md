# ZDI-26-169: GStreamer H.266 Codec Parser Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-169
- **ZDI-CAN:** ZDI-CAN-28910
- **Date:** 2026-03-06
- **CVE:** CVE-2026-3084
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GStreamer
- **Affected Products:** GStreamer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-169/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GStreamer. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of picture partitions. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GStreamer has issued an update to correct this vulnerability. More details can be found at: https://gitlab.freedesktop.org/gstreamer/gstreamer/-/commit/496e4f296e658fba7fd40027d3bbe6095633ec91

## Disclosure Timeline

- 2026-02-11 - Vulnerability reported to vendor
- 2026-03-06 - Coordinated public release of advisory
- 2026-03-06 - Advisory Updated
