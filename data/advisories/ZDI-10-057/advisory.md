# ZDI-10-057: Sun Java Runtime Environment JPEGImageDecoderImpl Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-057
- **ZDI-CAN:** ZDI-CAN-668
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0849
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-057/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun's Java Runtime. User interaction is required in that a user must be coerced into executing a malicious java application via visiting a website. The specific flaw exists within the JPEGImageDecoderImpl interface used by the image processing library to decode JPEG Imagery. By abusing an object meant to specify parameters used by the underlying jpeg decoder a malicious attacker can influence the decoding routine resulting in a heap overflow. This can be exploited to execute arbitrary code in the context of the application.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/javacpumar2010.html

## Disclosure Timeline

- 2010-01-15 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
