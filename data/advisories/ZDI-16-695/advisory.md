# ZDI-16-695: ARRIS VAP2500 Default Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-695
- **ZDI-CAN:** ZDI-CAN-3872
- **Date:** 2017-06-26
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ARRIS
- **Affected Products:** VAP2500
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-695/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ARRIS VAP2500. Authentication is not required to exploit this vulnerability. The specific flaw exists within the firmware and filesystem of the ARRIS VAP2500. The firmware and filesystem contain hard-coded default credentials in clear text. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

"ARRIS has taken the security vulnerabilities reported by the Zero Day Initiative for the ARRIS VAP2500 product seriously. The ARRIS VAP2500 product team worked quickly to develop a software update to resolve the reported vulnerabilities and shared the update with our service provider customers in October, 2016. As with many of the products we make, this update ultimately is delivered to the end user's equipment by their respective service provider. The reported vulnerabilities did not compromise video content or end users' personal data, but could have the potential to cause device stability problems in some unlikely circumstances."

## Disclosure Timeline

- 2016-08-09 - Vulnerability reported to vendor
- 2017-06-26 - Coordinated public release of advisory
