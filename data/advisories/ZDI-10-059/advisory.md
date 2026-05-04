# ZDI-10-059: Sun Java Runtime Environment JPEGImageEncoderImpl Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-059
- **ZDI-CAN:** ZDI-CAN-642
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0846
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-059/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun's Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within a function responsible for creating a JPEG image encoder. The function makes an invalid assignment based on the value of the num_components element of a comp_info structure while parsing a JPEG file. It then improperly uses the original value while performing memory copy operations. By specifying certain values as the num_components field this can be exploited to gain arbitrary code execution by overflowing an undersized buffer on the heap.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/javacpumar2010.html

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
