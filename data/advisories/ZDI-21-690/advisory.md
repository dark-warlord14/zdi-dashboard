# ZDI-21-690: OpenText Brava! Desktop TIF File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-690
- **ZDI-CAN:** ZDI-CAN-13677
- **Date:** 2021-06-15
- **CVE:** CVE-2021-31512
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** OpenText
- **Affected Products:** Brava! Desktop
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-690/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of OpenText Brava! Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Lt2dl 1.5.17.38

## Disclosure Timeline

- 2021-04-16 - Vulnerability reported to vendor
- 2021-06-15 - Coordinated public release of advisory
