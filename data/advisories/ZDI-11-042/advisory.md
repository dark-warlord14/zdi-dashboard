# ZDI-11-042: (0Day) Microsoft Office Excel Axis Properties Record Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-042
- **ZDI-CAN:** ZDI-CAN-904
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0978
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Aniway (Aniway.Anyway AT gmail DOT com) Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-042/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's usage of a specific field used for incrementing an index used in an array. Due to the application failing to verify the usage of the index into the array, the application will copy the contents of the specified element into a statically sized buffer on the stack. This can lead to code execution under the context of the application.

## Additional Details

Patched April 12, 2011 http://www.microsoft.com/technet/security/bulletin/ms11-021.mspx

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
