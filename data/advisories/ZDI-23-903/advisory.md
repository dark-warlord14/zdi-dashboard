# ZDI-23-903: GStreamer FLAC File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-903
- **ZDI-CAN:** ZDI-CAN-20775
- **Date:** 2023-07-06
- **CVE:** CVE-2023-37327
- **CVSS:** 7.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:H
- **Affected Vendors:** GStreamer
- **Affected Products:** GStreamer
- **Credit:** Michael Randrianantenaina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-903/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GStreamer. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of FLAC audio files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GStreamer has issued an update to correct this vulnerability. More details can be found at: https://gstreamer.freedesktop.org/security/sa-2023-0001.html

## Disclosure Timeline

- 2023-06-12 - Vulnerability reported to vendor
- 2023-07-06 - Coordinated public release of advisory
