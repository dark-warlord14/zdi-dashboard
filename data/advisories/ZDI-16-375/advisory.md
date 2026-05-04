# ZDI-16-375: Unitronics VisiLogic OPLC IDE vlp File Parsing Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-375
- **ZDI-CAN:** ZDI-CAN-3713
- **Date:** 2016-06-24
- **CVE:** CVE-2016-4519
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Unitronics
- **Affected Products:** VisiLogic OPLC IDE
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-375/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Unitronics VisiLogic OPLC IDE. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of a vlp file, which uses the zip file format. The software fails to validate the length of the filename field within the file before copying it to a stack buffer. This vulnerability can be leveraged by an attacker to achieve code execution within the context of the process.

## Additional Details

Unitronics has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-175-02

## Disclosure Timeline

- 2016-04-28 - Vulnerability reported to vendor
- 2016-06-24 - Coordinated public release of advisory
