# ZDI-16-672: Fatek Automation PLC WinProladder Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-672
- **ZDI-CAN:** ZDI-CAN-3705
- **Date:** 2016-12-15
- **CVE:** CVE-2016-8377
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/Au:M/C:C/I:C/A:C
- **Affected Vendors:** Fatek Automation
- **Affected Products:** PLC WinProladder
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-672/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fatek Automation PLC WinProladder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PLC configuration data from a network source. The process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

Fatek Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-350-01

## Disclosure Timeline

- 2016-09-27 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
