# ZDI-18-435: Rockwell Automation Arena File Parsing SmAnim Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-435
- **ZDI-CAN:** ZDI-CAN-5496
- **Date:** 2018-05-14
- **CVE:** CVE-2018-8843
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** Arena
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-435/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Rockwell Automation Arena. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of an Arena Model file. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the Arena process.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-130-02

## Disclosure Timeline

- 2018-01-10 - Vulnerability reported to vendor
- 2018-05-14 - Coordinated public release of advisory
- 2018-05-14 - Advisory Updated
