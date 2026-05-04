# ZDI-17-642: Adobe Digital Editions ePub Font Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-642
- **ZDI-CAN:** ZDI-CAN-4127
- **Date:** 2017-08-09
- **CVE:** CVE-2017-11274
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Digital Editions
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-642/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Digital Editions. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of fonts in ePub files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/Digital-Editions/apsb17-27.html

## Disclosure Timeline

- 2016-11-03 - Vulnerability reported to vendor
- 2017-08-09 - Coordinated public release of advisory
