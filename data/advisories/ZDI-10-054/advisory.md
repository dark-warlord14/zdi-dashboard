# ZDI-10-054: Sun Java Runtime Environment JPEGImageReader stepX Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-054
- **ZDI-CAN:** ZDI-CAN-641
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0841
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-054/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun's Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the processing of JPEG image dimensions. When specifying large values to the dimensions of a subsample an integer overflow occurs leading to memory corruption. Successful exploitation of this vulnerability can lead to a compromise under the credentials of the currently logged in user.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/javacpumar2010.html

## Disclosure Timeline

- 2009-12-10 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
