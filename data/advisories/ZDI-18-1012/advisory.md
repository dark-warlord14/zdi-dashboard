# ZDI-18-1012: Fuji Electric V-Server VPR File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1012
- **ZDI-CAN:** ZDI-CAN-5889
- **Date:** 2018-09-12
- **CVE:** CVE-2018-14823
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Fuji Electric
- **Affected Products:** V-Server
- **Credit:** Ghirmay Desta
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fuji Electric V-Server. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of a VPR file. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-254-01

## Disclosure Timeline

- 2018-03-08 - Vulnerability reported to vendor
- 2018-09-12 - Coordinated public release of advisory
- 2018-09-12 - Advisory Updated
