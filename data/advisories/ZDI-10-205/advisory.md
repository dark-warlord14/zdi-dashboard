# ZDI-10-205: Oracle Sun JRE JPEGImageWriter.writeImage Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-205
- **ZDI-CAN:** ZDI-CAN-809
- **Date:** 2010-10-12
- **CVE:** CVE-2010-3565
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-205/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun's Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the processing of JPEG image dimensions. When specifying large values to the dimensions of a subsample an integer overflow occurs leading to memory corruption. Successful exploitation of this vulnerability can lead to remote compromise under the credentials of the currently logged in user.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuoct2010-176258.html

## Disclosure Timeline

- 2010-06-17 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
