# ZDI-25-467: GStreamer H266 Codec Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-467
- **ZDI-CAN:** ZDI-CAN-27381
- **Date:** 2025-07-03
- **CVE:** CVE-2025-6663
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GStreamer
- **Affected Products:** GStreamer
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-467/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GStreamer. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of H266 sei messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GStreamer has issued an update to correct this vulnerability. More details can be found at: https://gitlab.freedesktop.org/tpm/gstreamer/-/commit/eedd01ac3dfeb60e36a44bb61a6d0418454e8416

## Disclosure Timeline

- 2025-06-23 - Vulnerability reported to vendor
- 2025-07-03 - Coordinated public release of advisory
- 2025-07-03 - Advisory Updated
