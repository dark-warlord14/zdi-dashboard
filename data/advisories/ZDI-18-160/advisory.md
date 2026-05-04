# ZDI-18-160: Fuji Electric V-Server VPR File Parsing Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-160
- **ZDI-CAN:** ZDI-CAN-5383
- **Date:** 2018-02-12
- **CVE:** CVE-2018-5442
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:P
- **Affected Vendors:** Fuji Electric
- **Affected Products:** V-Server
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-160/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fuji Electric V-Server. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of project files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-032-01

## Disclosure Timeline

- 2017-11-24 - Vulnerability reported to vendor
- 2018-02-12 - Coordinated public release of advisory
- 2018-02-12 - Advisory Updated
