# ZDI-10-211: RealNetworks Realplayer RecordClip Parameter Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-211
- **ZDI-CAN:** ZDI-CAN-643
- **Date:** 2010-10-15
- **CVE:** CVE-2010-3749
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Sean de Regge
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-211/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the browser plugins provided by RealNetworks. The RecordClip method can be access via the ActiveX control or the Firefox plugin. By injecting a specific character into the arguments to this method, invalid parameters can be passed to a child process that is launched on the local system. This parameter injection allows an attacker to download and subsequently execute a file on a target system, thus allowing for remote code execution.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/10152010_player/en/

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-10-15 - Coordinated public release of advisory
