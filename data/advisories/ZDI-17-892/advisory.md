# ZDI-17-892: Foxit Reader Document author Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-892
- **ZDI-CAN:** ZDI-CAN-5282
- **Date:** 2017-11-14
- **CVE:** CVE-2017-16581
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-892/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the author attribute of the Document object. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2017-10-11 - Vulnerability reported to vendor
- 2017-11-14 - Coordinated public release of advisory
