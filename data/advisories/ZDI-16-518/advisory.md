# ZDI-16-518: Rockwell Automation RSLogix Micro Starter Lite Project File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-518
- **ZDI-CAN:** ZDI-CAN-3793
- **Date:** 2016-09-19
- **CVE:** CVE-2016-5814
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** RSLogix Micro Starter Lite
- **Credit:** Ariele Caltabiano [kimiya]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-518/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Rockwell Automation RSLogix Micro Starter Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of a RSS (project) file. The issue lies in the failure to properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-224-02

## Disclosure Timeline

- 2016-06-02 - Vulnerability reported to vendor
- 2016-09-19 - Coordinated public release of advisory
