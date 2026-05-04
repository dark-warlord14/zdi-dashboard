# ZDI-11-114: RealNetworks Helix Server x-wap-profile Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-114
- **ZDI-CAN:** ZDI-CAN-921
- **Date:** 2011-04-01
- **CVE:** CVE-2010-4235
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** Helix Server
- **Credit:** defrost
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-114/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Helix Server products. Authentication is not required to exploit this vulnerability. The specific flaw exists within the rmserver.exe process. This process is active by default on all Helix Server installations. Due to a failure to properly sanitize the contents of the 'x-wap-profile' header, it is possible to provide malicious data that is passed directly to a format string function. Remote attackers could leverage this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://www.realnetworks.com/helix-support/security-updates.aspx

## Disclosure Timeline

- 2010-10-02 - Vulnerability reported to vendor
- 2011-04-01 - Coordinated public release of advisory
