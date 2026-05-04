# ZDI-18-263: (Pwn2Own) Mozilla Firefox libvorbis OGG Decoding Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-263
- **ZDI-CAN:** ZDI-CAN-5822
- **Date:** 2018-03-23
- **CVE:** CVE-2018-5146
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-263/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the libvorbis library. A crafted Vorbis audio file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2018-08/

## Disclosure Timeline

- 2018-03-18 - Vulnerability reported to vendor
- 2018-03-23 - Coordinated public release of advisory
- 2018-03-23 - Advisory Updated
