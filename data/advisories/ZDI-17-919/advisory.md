# ZDI-17-919: EMC Unisphere For VMAX vApp Manager ORBServlet Remote Credential Creation Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-919
- **ZDI-CAN:** ZDI-CAN-5070
- **Date:** 2017-11-20
- **CVE:** CVE-2017-14375
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** EMC
- **Affected Products:** Unisphere For VMAX
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-919/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of EMC Unisphere For VMAX vApp Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ORBServlet. The vulnerability is caused by improper access controls that allow the creation of admin credentials. An attacker can leverage this vulnerability to disclose sensitive information under the context of the web application.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/fulldisclosure/2017/Oct/70

## Disclosure Timeline

- 2017-08-04 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
