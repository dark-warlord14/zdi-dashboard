# ZDI-11-059: (0Day) CA ETrust Secure Content Manager Common Services Transport Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-059
- **ZDI-CAN:** ZDI-CAN-342
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0758
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** CA
- **Affected Products:** eTrust Secure Content Manager
- **Credit:** Sebastian Apelt (sebastian.apelt@siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-059/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Computer Associates eTrust Secure Content Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists in the eTrust Common Services Transport (ECSQdmn.exe) running on port 1882. When making a request to this service a user supplied DWORD value is used in a memory copy operation. Due to the lack of bounds checking an integer can be improperly calculated leading to a heap overflow. If successfully exploited this vulnerability will result in a remote system compromise with SYSTEM credentials.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID={EE6F16E1-6E05-4890-A739-2B9F745C721F}

## Disclosure Timeline

- 2008-05-23 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
