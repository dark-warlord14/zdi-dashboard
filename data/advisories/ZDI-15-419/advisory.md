# ZDI-15-419: Symantec Ghost Out-Of-Bounds Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-419
- **ZDI-CAN:** ZDI-CAN-2989
- **Date:** 2015-09-03
- **CVE:** CVE-2015-5689
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Symantec
- **Affected Products:** Ghost
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-419/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Ghost. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Ghost images. The issue lies in sign-extending byte values from an array before using them as an index into an array, allowing for out-of-bounds access. An attacker can leverage this vulnerability to execute arbitrary code within the context of the current process.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=&suid=20150902_00

## Disclosure Timeline

- 2015-06-02 - Vulnerability reported to vendor
- 2015-09-03 - Coordinated public release of advisory
