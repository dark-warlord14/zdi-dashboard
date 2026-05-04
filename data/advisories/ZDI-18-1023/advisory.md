# ZDI-18-1023: Fuji Electric V-Server Lite File Parsing Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1023
- **ZDI-CAN:** ZDI-CAN-6376
- **Date:** 2018-09-12
- **CVE:** CVE-2018-10637
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Fuji Electric
- **Affected Products:** V-Server Lite
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1023/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fuji Electric V-Server Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of VPR files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-254-02

## Disclosure Timeline

- 2018-06-12 - Vulnerability reported to vendor
- 2018-09-12 - Coordinated public release of advisory
- 2018-09-12 - Advisory Updated
