# ZDI-10-249: Apple Quicktime Sorenson Video Codec Decoding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-249
- **ZDI-CAN:** ZDI-CAN-732
- **Date:** 2010-11-10
- **CVE:** CVE-2010-3793
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-249/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way QuickTime decompresses video samples that are encoded with the Sorenson v3 Codec. Upon parsing malformed video sample data, the application will calculate an index for decompression and use that to seek into a buffer used for writing. Due to lack of bounds checking on the index, a pointer can be made to point outside of the target array. Upon writing of the data a memory corruption will occur. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Fixed in Mac OS X 10.6.5: http://support.apple.com/kb/HT4435 QuickTime 7.6.9: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-03-22 - Vulnerability reported to vendor
- 2010-11-10 - Coordinated public release of advisory
