# ZDI-11-074: Adobe Reader u3d Parent Node Count Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-074
- **ZDI-CAN:** ZDI-CAN-946
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0600
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** el
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-074/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader on Mac OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the U3D component distributed with the Reader. The application uses the Parent Node count to calculate the size of an allocation. This value is not properly validated and the result of this size calculation can be wrapped to an unexpectedly small and insufficient value. Writes to this newly allocated buffer can be outside the bounds of its allocation. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-03.html

## Disclosure Timeline

- 2010-11-15 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
