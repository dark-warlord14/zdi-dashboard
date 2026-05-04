# ZDI-16-163: Dell SonicWALL GMS Virtual Appliance Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-163
- **ZDI-CAN:** ZDI-CAN-3137
- **Date:** 2016-02-10
- **CVE:** CVE-2016-2397
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SonicWALL
- **Affected Products:** GMS Virtual Appliance
- **Credit:** cpnrodzc7
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-163/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Dell SonicWALL GMS Virtual Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the cliserver implementation, which accepts, deserializes, and executes XML-encoded, serialized Java code. An attacker can leverage this vulnerability to execute arbitrary code under the context of root.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://www.mysonicwall.com/firmware/downloadcenter.aspx Hotfix 168056

## Disclosure Timeline

- 2015-09-13 - Vulnerability reported to vendor
- 2016-02-10 - Coordinated public release of advisory
